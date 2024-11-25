import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import store from "store";

import { Provider } from "react-redux";

import Error404 from "containers/errors/error404";
import Home from "containers/pages/HomeTemp";
import FloresCbd from "containers/pages/Flores_cbd";
import AceiteCbd from "containers/pages/Aceite_cbd";
import VaperCbd from "containers/pages/Vaper_cbd";
import PackCbd from "containers/pages/Packs_cbd";
import FisioCbd from "containers/pages/Fisio_cbd";

function App() {
  return (
    <Provider store={store}>
      
      <Router>
        <Routes>
          <Route path="*" element={<Error404 />} /> 
          <Route path="/" element={<Home/>} />
          <Route path="/flores-cbd" element={<FloresCbd/>} /> 
          <Route path="/aceite-cbd" element={<AceiteCbd/>} /> 
          <Route path="/vaper-cbd" element={<VaperCbd/>} /> 
          <Route path="/pack-cbd" element={<PackCbd/>} /> 
          <Route path="/fisioterapia-cbd" element={<FisioCbd/>} />  
        </Routes>
      </Router>
    </Provider>
  );

}

export default App;
