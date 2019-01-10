import React from "react";
import PropTypes from "prop-types";

class Confirmation extends React.Component {
  render() {
    return (
      <div>
        <div>
          <svg
            className="checkmark"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 52 52"
          >
            <circle
              className="checkmark__circle"
              cx="26"
              cy="26"
              r="25"
              fill="none"
            />
            <path
              className="checkmark__check"
              fill="none"
              d="M14.1 27.2l7.1 7.2 16.7-16.8"
            />
          </svg>
        </div>
        <h3>We have received your complaint</h3>
        <h4>Your case number: {this.props.caseNumber}</h4>
        <div>
          Thank you for sharing your experience with us. Our job is to make sure
          your complaint is investigated fairly, thoroughly, and transparently.
          This helps to serve you better.
        </div>
        <div>
          If you provided an email, you will recieve an email with a
          confirmation number for your complaint. You can also{" "}
          <a href="mailto:fake@email.address">email us</a> or call us at
          512-974-9090 at any time with your confirmation number to find your
          complaint in this process.
        </div>
      </div>
    );
  }
}

export default Confirmation;
