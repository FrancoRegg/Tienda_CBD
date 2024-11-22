import Footer from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import Layout from "hocs/layouts/Layout"

function Home() {
    
    return(
        <Layout>
           <NavBar/>
           <div className="py-20">
           <img src="/logo192.png" alt="Logo" />
           </div>
            <Footer/>
        </Layout>
    )
}

export default Home