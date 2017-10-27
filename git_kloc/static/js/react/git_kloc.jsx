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
          class="btn btn-primary"
          onClick={this.handleLoginButton}>
          Login
        </button>
      </div>
    )
  }
}


ReactDOM.render(
  <LoginView />,
  document.getElementById('git-kloc')
);
