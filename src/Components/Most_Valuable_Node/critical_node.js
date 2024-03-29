import React from 'react'
import {Card} from 'semantic-ui-react'
import {Link} from 'react-router-dom'

const most_critical_node = ({name,solution}) =>{
    
    return(
        <Card>
            <Card.Content>
                <Card.Header><h1>Most Critical Part of Ecosystem</h1></Card.Header>
                <Card.Meta>
                    <h5>Security Advice</h5>
                </Card.Meta>
                <Card.Description>
                    <h3>{name}</h3>
                    <p>Through our analysis we found that {name} is the most imporant part for your whole personal account ecosystem, as it has the most connections to other accounts.</p>
                    <h3>Recommendation(s)</h3>
                    <p>{solution}</p>
                    <Link to='/tools'>See more password generation options</Link>
                </Card.Description>
            </Card.Content>
         </Card>
    )
}


export default most_critical_node
