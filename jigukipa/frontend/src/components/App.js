import React, { Component, Fragment } from "react";
import ReactDOM, { render } from "react-dom";

import Header from "./layout/Header";
import Kipa from "./kipa/Kipa";

import { Provider } from "react-redux";
import store from "../store";

export class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="container-fluid">
            <Kipa />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
