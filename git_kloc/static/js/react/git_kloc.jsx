import React from 'react';
import ReactDOM from 'react-dom';


class VCS extends React.Component {
  render() {
    return (
      <div class="vcs">
        List of VCS here
      </div>
    )
  }
}


ReactDOM.render(
  <VCS />,
  document.getElementById('git-kloc')
);
