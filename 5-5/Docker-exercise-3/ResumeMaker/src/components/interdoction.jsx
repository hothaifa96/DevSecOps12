import { Link } from "react-router-dom";

const Inderdoction = () => {
  return (
    <div style={{ marginTop: "20vh" }}>
      <div className="container-inter px-3">
        <h1>Build your own resume</h1>
        <p className="lead" >
          Using our brand new resume creator you can building simple and
          beautiful resume with minimum and max performance, just add your
          own beautiful personality and find the jox you were dreaming on.
        </p>
        <p className="lead" >
          <Link to="/tamplate">
            <a className="btn btn-lg btn-secondary fw-bold border-white bg-white">
              Start building
            </a>
          </Link>
        </p>
      </div>


    </div>


  );
};

export default Inderdoction;
