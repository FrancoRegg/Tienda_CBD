import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function FloresCbd() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="py-20">
            FLORESCBD
            </div>
            <Footer/>
        </Layout>
    )
}

export default FloresCbd