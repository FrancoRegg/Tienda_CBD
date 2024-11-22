import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function Categoria1() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="py-20">
            Categoria1
            </div>
            <Footer/>
        </Layout>
    )
}

export default Categoria1