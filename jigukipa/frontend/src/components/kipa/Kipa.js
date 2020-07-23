import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPosts } from "../../actions/kipa";
// import { Link } from "react-router-dom";

export class Kipa extends Component {
  static propTypes = {
    Posts: PropTypes.array.isRequired,
    getPosts: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getPosts();
  }

  render() {

    return (
      <Fragment>
        <div className="container-fluid">
          <h2>Posts</h2>

    
            {this.props.Posts.map((post) => (
              <h2 key={post.id}>{post.caption}</h2>
            ))}
          </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
    Posts: state.Kipa.Posts,
  });

export default connect(mapStateToProps, {getPosts})(Kipa);
