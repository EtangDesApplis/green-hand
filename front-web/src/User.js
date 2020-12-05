import React, { Component } from 'react'
import Form from "react-bootstrap/Form";
//import Popup from "reactjs-popup";


/*
 * User definition
 * get the input user information inputs
 */

class User extends Component {
    initialState = {
        email: '',
        name: '',
    }

    state = this.initialState

        handleChange = (event) => {
            const {name, value} = event.target

            this.setState({
                [name]: value
            })
    }
        
    submitForm = () => {

        this.props.sendInfo(this.state)
        this.setState(this.initialState)

    }
    render() {
        const { email , name} = this.state;

        return (
             <>
                <Form>
                    <Form.Group>
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="text"
                            name="email"
                            id="email"
                            value={email}
                            onChange={this.handleChange} placeholder="Enter email" />
                        <Form.Text className="text-muted">Please type email</Form.Text>
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Name</Form.Label>
                        <Form.Control type="text"
                            name="name"
                            id="name"
                            value={name}
                            onChange={this.handleChange} placeholder="Enter name" />
                        <Form.Text className="text-muted">Please type name</Form.Text>
                    </Form.Group>
                    <input type="button" value="Submit" onClick={this.submitForm} />
                </Form>
                
             </>  

        );
    }
}
export default User;