import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import store from "store";

import { Provider } from "react-redux";

import Error404 from "containers/errors/error404";
import Home from "containers/pages/HomeTemp";
import Categoria1 from "containers/pages/Categoria1";
import Categoria2 from "containers/pages/Categoria2";
import Categoria3 from "containers/pages/Categoria3";
import Categoria4 from "containers/pages/Categoria4";
import Categoria5 from "containers/pages/categoria5";


function App() {
  return (
    <Provider store={store}>
      
      <Router>
        <Routes>
          <Route path="*" element={<Error404 />} /> 
          <Route path="/" element={<Home/>} />
          <Route path="/categoria1" element={<Categoria1/>} /> 
          <Route path="/categoria2" element={<Categoria2/>} /> 
          <Route path="/categoria3" element={<Categoria3/>} /> 
          <Route path="/categoria4" element={<Categoria4/>} /> 
          <Route path="/categoria5" element={<Categoria5/>} />  
        </Routes>
      </Router>
    </Provider>
  );

}

export default App;
