import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function Home() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="pt-28">
           PAGINA INICIO
           </div>
           <Footer/>
        </Layout>
    )
}

export default Home