import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function VaperCbd() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="pt-28">
            VAPERS CBD
            </div>
            <Footer/>
        </Layout>
    )
}

export default VaperCbd