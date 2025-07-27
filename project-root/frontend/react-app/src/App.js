import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    axios.get("http://localhost:8080/api/hello")
      .then(res => setMsg(res.data))
      .catch(console.error);
  }, []);

  return <div>{msg}</div>;
}

export default App;