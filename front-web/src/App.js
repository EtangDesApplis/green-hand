import React, { Component } from 'react'
import Table from './Table'
import Formulaire from './Formulaire'
import User from './User'
//import Popup from './Popup'
import Popup from "reactjs-popup";
//import 'reactjs-popup/dist/index.css';
/*
 * App definition
 * Centralize the app
 */


class App extends Component {
    state = {
        characters: [],
        showPopup: false , 
    }
    removeCharacter = (index) => {
        const { characters } = this.state

        this.setState({
            characters: characters.filter((character, i) => {
                return i !== index
            }),
        })
    }
    
    togglePopup() {
        
        this.setState({
            characters: [],
            showPopup: false, 
        });
    }  

    handleSubmit = (character) => {
        this.setState({ characters: [...this.state.characters, character] })
    }
    sendInfo = (characters) => {

        const seedsValue = [...this.state.characters]
        if (seedsValue != null) {
            for (var i = 0, l = seedsValue.length; i < l; i++) {
                if (seedsValue[i].seedingOutdoor[0] !== '') {
                    seedsValue[i].seedingOutdoor = seedsValue[i].seedingOutdoor.map((month) => (month.value))
                }
                if (seedsValue[i].seedingIndoor[0] !== '') {
                    seedsValue[i].seedingIndoor = seedsValue[i].seedingIndoor.map((month) => (month.value))
                }
                if (seedsValue[i].harvest[0] !== '') {
                    seedsValue[i].harvest = seedsValue[i].harvest.map((month) => (month.value))
                }
            }

         }
  

        
        console.log(JSON.stringify({
            email: characters.email,
            name: characters.name,
            info: "",
            seeds: seedsValue
        }))
        
        

        fetch('https://chefphan.com/gh-api/', {
                method: 'POST',
                body: JSON.stringify({
                    email: characters.email,
                    name: characters.name,
                    info: "",
                    seeds: seedsValue
                }),
            headers: {
                "access-control-allow-origin": "*",
                'Content-Type': 'application/json'
            }
        })
                .then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Success:', response));

        this.setState({
            showPopup: true,
            characters: [],
        })
        

    }
    render() {
        const { characters } = this.state

        return (
            <div className="container">
                <User sendInfo={this.sendInfo} />
                <Popup open={this.state.showPopup}  >                   
                    <h1 className="text-center"> Table Submited</h1><br/>
                    <div className="text-center">
                    <button onClick={this.togglePopup.bind(this)} className="text-center">OK</button></div>              
                    
                </Popup>                  
                <Table characterData={characters} removeCharacter={this.removeCharacter} />
                <Formulaire handleSubmit={this.handleSubmit} />
            </div>
        )
    }
}

export default App
