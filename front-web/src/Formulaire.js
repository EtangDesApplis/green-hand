import React, { Component } from 'react'
import Form from "react-bootstrap/Form";
import Select from 'react-select';
/*
 * Formular definition
 * the add buttun add a line in the Table
 */

const month = [
    { label: 'January', value: '1' },
    { label: 'February', value: '2' },
    { label: 'March', value: '3' },
    { label: 'April', value: '4' },
    { label: 'May', value: '5' },
    { label: 'June', value: '6' },
    { label: 'July', value: '7' },
    { label: 'August', value: '8' },
    { label: 'September', value: '9' },
    { label: 'October', value: '10' },
    { label: 'November', value: '11' },
    { label: 'December', value: '12' },
];

class Formulaire extends Component {

    initialState = {
        variety: '',
        seedingOutdoor: [""],
        seedingIndoor: [""],
        harvest: [""],
        exposition: '',
        timeToHarvest: '',
    }

    state = this.initialState
  
    handleMonthChange = (opt, meta) => {

        const  name  = meta.name
        var options = opt;    
        var value = [];
        if (options == null) {
            this.setState({
                [name]: ""
            })
        }
        else {
             for (var i = 0, l = options.length; i < l; i++) {
                value.push(options[i].value);
             }
        }
        this.setState({
            [name]: value
        })

    }

    handleMonthChange = (selectedOptions,meta) => {
        const name = meta.name
        this.setState({
            [name]: selectedOptions
        })
    }


    handleChange = (event) => {
         const {name, value} = event.target
         this.setState({
            [name]: value
         })
    }
    
    addForm = () => {
        this.props.handleSubmit(this.state)
        this.setState(this.initialState)
    }

    render() {
        const {variety, seedingOutdoor, seedingIndoor, harvest, exposition, timeToHarvest} = this.state;

        return (
             <>
                <Form>   
                    <Form.Group>
                        <Form.Label>Variety</Form.Label>
                        <Form.Control type="text"
                            name="variety"
                            id="variety"
                            value={variety}
                            onChange={this.handleChange} placeholder="Enter plant variety" />
                        <Form.Text className="text-muted">Please type plant variety</Form.Text>
                    </Form.Group>                   
                    <Form.Label>Seeding Outdoor</Form.Label>
                    <Select
                        name="seedingOutdoor"
                        id="seedingOutdoor"
                        options={month}
                        value={seedingOutdoor}
                        isMulti
                        onChange={this.handleMonthChange}
                    />                    
                    <Form.Label>Seeding Indoor</Form.Label>
                    <Select
                        name="seedingIndoor"
                        id="seedingIndoor"
                        options={month}
                        value={seedingIndoor}
                        isMulti
                        onChange={this.handleMonthChange}
                    />
                    <Form.Label>Harvest</Form.Label>
                    <Select
                        name="harvest"
                        id="harvest"
                        options={month}
                        value={harvest}
                        isMulti
                        onChange={this.handleMonthChange}
                    />                    
                    <Form.Group>
                        <Form.Label>Exposition</Form.Label>
                        <Form.Control as="select" name="exposition" id="exposition" value={exposition} onChange={this.handleChange} >
                            <option value="sunny">Sunny</option>
                            <option value="half-shadow">Half Shadow</option>
                            <option value="shadow">Shadow</option>
                        </Form.Control>
                        <Form.Text className="text-muted">Please choose what exposition the plant needs</Form.Text>
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Time to harvest</Form.Label>
                        <Form.Control type="text"
                            name="timeToHarvest"
                            id="timeToHarvest"
                            value={timeToHarvest}
                            onChange={this.handleChange} placeholder="Enter days before harvest" />
                        <Form.Text className="text-muted">Please type the time in days after seeding to harvest the first vegetable</Form.Text>
                    </Form.Group>
                    <input type="button" value="Add" onClick={this.addForm} />
                </Form>               
             </>  
        );
    }
}
export default Formulaire;