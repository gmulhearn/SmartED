import React, { useEffect } from 'react';
import StudentApp from './StudentApp';
import TeacherApp from './TeacherApp';
import axios from 'axios';
import Cookies from 'js-cookie';
import Favicon from 'react-favicon';

// DETERMINE LOCATION
var url;
if (typeof Cookies.get('EAIT_WEB') !== "undefined") {
  // console.log("ON DECO SITE");
  url = "https://deco3801-pogware.uqcloud.net";
} else {
  // console.log("ON LOCAL");
  url = "http://localhost:8000";
}
console.log("location: " + url);
//

const App = () => {
  const [user, setUser] = React.useState(null);

  let force_teacher;

  localStorage.getItem("force_teacher") === "1" ? force_teacher = 1 : force_teacher = 0;

  console.log("FORCE TEACHER: ", force_teacher);

  useEffect(() => {
    let method;

    force_teacher === 1 ? method = "get" : method = "delete";

    axios(url+'/Database/force-teacher/', {
      method: method,
      withCredentials: true
    }).then(res => {
      console.log("force teacher with method: ", method);

      axios(url+'/Database/initialize/', {
        method: "get",
        withCredentials: true
      }).then(res => {
        setUser(res.data);
      })
    }) 
  }, []);

  return (
    <div>
      <Favicon url="http://clipartmag.com/images/graduation-cap-png-24.png" />
      {user !== null && (user.is_student === 0 ? <TeacherApp user={user} /> : <StudentApp user={user} />)}
    </div>
  );
}

export default App;