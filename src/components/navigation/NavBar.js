import { connect } from "react-redux"
import './../../styles/NavBar.css'
import { Link } from "react-router-dom"

function NavBar(){
    return(
        <nav className="nav">
            <div className="nav-container">
            <div className="nav-container-items">
                <div className="nav-logo">
                    <Link to='/'>Logo de Marca</Link>
                </div>
                <div className="nav-container-categorias">
                    <Link to='/categoria1'className="categorias">Categoria 1</Link>
                    <Link to='/categoria2'className="categorias">Categoria 2</Link>
                    <Link to='/categoria3'className="categorias">Categoria 3</Link>
                    <Link to='/categoria4'className="categorias">Categoria 4</Link>
                    <Link to='/categoria5'className="categorias">Categoria 5</Link>
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