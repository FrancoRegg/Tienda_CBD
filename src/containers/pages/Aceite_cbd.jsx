import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function AceiteCbd() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="py-20">
            ACEITE CBD
            </div>
            <Footer/>
        </Layout>
    )
}

export default AceiteCbd