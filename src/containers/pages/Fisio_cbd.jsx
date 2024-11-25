import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function FisioCbd() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="pt-28">
            FISIOTERAPIA CBD
            </div>
            <Footer/>
        </Layout>
    )
}

export default FisioCbd