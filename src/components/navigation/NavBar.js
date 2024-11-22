import { connect } from "react-redux"
//import './../../styles/NavBar.css'

function NavBar(){
    return(
        <nav className="w-full bg-black">
            navbar
        </nav>
    )
}

const mapStateToProps = state => ({})

export default connect(mapStateToProps,{}) (NavBar)