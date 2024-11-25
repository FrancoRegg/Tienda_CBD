import { connect } from "react-redux"
import './../../styles/NavBar.css'
import { Link, NavLink } from "react-router-dom"
//import logo1 from "./../../assets/image/logocbd.png"
import logo from "./../../assets/image/logocbd-sin-fondo.png"

function NavBar(){
    return(
        <nav className="nav">
            <div className="nav-container">
            <div className="nav-container-items">
                <div className="nav-logo">
                    <Link to='/'><img src={logo} alt="Leafy" className="nav-imagen"/></Link>
                </div>
                <div className="nav-container-categorias">
                    <NavLink to='/flores-cbd'className="categorias">flores cbd</NavLink>
                    <NavLink to='/aceite-cbd'className="categorias">aceite cbd</NavLink>
                    <NavLink to='/vaper-cbd'className="categorias">vaper cbd</NavLink>
                    <NavLink to='/pack-cbd'className="categorias">packs cbd</NavLink>
                    <NavLink to='/fisioterapia-cbd'className="categorias">fisioterapia cbd</NavLink>
                </div>
                <div className="nav-container-usuario">
                    <Link to=''><i class="bi bi-person-circle icon"></i></Link>
                    <Link to=''><i class="bi bi-cart3 icon"></i></Link>
                </div>
            </div>
            </div>
        </nav>
    )
}

const mapStateToProps = state => ({})

export default connect(mapStateToProps,{}) (NavBar)