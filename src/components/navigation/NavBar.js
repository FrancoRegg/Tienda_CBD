import { connect } from "react-redux"
import './../../styles/NavBar.css'
import { Link, NavLink } from "react-router-dom"
import logo from "./../../assets/image/logocbd.png"

function NavBar(){
    return(
        <nav className="nav">
            <div className="nav-container">
            <div className="nav-container-items">
                <div className="nav-logo">
                    <Link to='/'><img src={logo} alt="Leafy" className="nav-imagen"/></Link>
                </div>
                <div className="nav-container-categorias">
                    <NavLink to='/categoria1'className="categorias">Categoria 1</NavLink>
                    <NavLink to='/categoria2'className="categorias">Categoria 2</NavLink>
                    <NavLink to='/categoria3'className="categorias">Categoria 3</NavLink>
                    <NavLink to='/categoria4'className="categorias">Categoria 4</NavLink>
                    <NavLink to='/categoria5'className="categorias">Categoria 5</NavLink>
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