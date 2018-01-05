import React from 'react';
import ReactDOM from 'react-dom';


class LoginView extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginButton = this.handleLoginButton.bind(this);
  }
  handleLoginButton() {
    fetch(
      '/login',
      {credentials: 'include'}
    )
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      if (data.auth_url) {
        window.location.href = data.auth_url;
      }
    });
  }
  render() {
    return (
      <div>
        <button
          className="btn btn-primary"
          onClick={this.handleLoginButton}>
          Login via github
        </button>
      </div>
    )
  }
}

class Repository extends React.Component {
  render() {
    return (
      <li className="list-group-item">
        {this.props.repo}
      </li>
    )
  }
}

class Repositories extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'repositories': []
    }
  }
  componentDidMount() {
    fetch(
      '/repositories.json',
      {credentials: 'include'}
    )
    .then(response => {
      return response.json();
    })
    .then(data => {
      if (data.repos) {
        this.setState({'repositories': data.repos});
      }
    });
  }
  render() {
    var repos = this.state.repositories.map((repo, index) => {
      return (<Repository key={index} repo={repo} />);
    });
    return (
      <div><ul className="list-group"> {repos} </ul></div>
    )
  }
}

class MainComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'isLoggedIn': false,
      'context': ''
    }
  }

  componentDidMount() {
    fetch(
      '/is_logged_in',
      {credentials: 'include'}
    )
    .then(response => {
      return response.json();
    })
    .then(data => {
      this.setState({'isLoggedIn': data.isLoggedIn});
    });
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    if (isLoggedIn) {
      return (<Repositories />)
    } else {
      return (<LoginView />)
    }
  }
}


ReactDOM.render(
  <MainComponent />,
  document.getElementById('git-kloc')
);
