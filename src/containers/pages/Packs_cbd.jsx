import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function PackCbd() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="py-20">
            PACKS CBD
            </div>
            <Footer/>
        </Layout>
    )
}

export default PackCbd