import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from "axios";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current_time: ""
    }
    this.loadTime = this.loadTime.bind(this);
  }
  componentDidMount() {
    setInterval(this.loadTime, 1000)

  }
  async loadTime() {
    const promise = await axios.get("http://127.0.0.1:5000/current_time");
    const current_time = promise.data;
    this.setState({ current_time })
  }
  render() {
    return (
      <h1 style={{ textAlign: "center" }}>Current Time : {this.state.current_time}</h1>
    );
  }
}

