import React from 'react';
import ReactDOM from 'react-dom';


class VCS extends React.Componet {
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
