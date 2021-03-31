import React from 'react'
import {Card, List} from 'semantic-ui-react'

const header = ({name,solution}) =>{
    
    return(
        <Card>
            <Card.Content>
                <Card.Header><h1>Potential Security Issue</h1></Card.Header>
                <Card.Meta>
                    <h5>Password Strength Issue</h5>
                </Card.Meta>
                <Card.Description>
                    <h3>{name}</h3>
                    <p>You use the password <b>'{name}'</b> to access more than one account. If a hacker steals <b>'{name}'</b> then you have compramised every account where that password is used.</p>
                    <h3>Recommendation(s)</h3>
                    {solution}
                </Card.Description>
            </Card.Content>
        </Card>
    )
}


export default header