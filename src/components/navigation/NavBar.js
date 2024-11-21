import { connect } from "react-redux"

function NavBar(){
    return(
        <nav>
            navbar
        </nav>
    )
}

const mapStateToProps = state => ({})

export default connect(mapStateToProps,{}) (NavBar)