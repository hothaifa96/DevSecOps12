import "../index.css";
import React from "react";
import avatar from "../images/avatar.jpeg";
import femaleAvatar from "../images/femaleAvatar.png";

const FinnalDisplay = (props) => {
  ///declare the props/////
  const { personalInfo, about, expiriense, educaition, techs, tamplate } =
    props.resume;

  ///personal info functions/////
  let pickedTamplate = "subpage" + tamplate; ///control backround style
  let fullName = personalInfo.firstName + " " + personalInfo.lastName;

  let languages = "";
  for (let i = 0; i < personalInfo.Language.length; i++) {
    ///sets langueges string
    let x = " ";
    let y = ", ";
    if (languages == "") languages = languages + x + personalInfo.Language[i];
    else languages = languages + y + personalInfo.Language[i];
  }
  //control avatar gender
  let avatrImg = femaleAvatar;
  if (personalInfo.gender == "male") avatrImg = avatar;
  else if (personalInfo.gender == "male") avatrImg = femaleAvatar;

  ////prefessional skills functions///
  let bestLevel = { width: techs.best.level + "%" }; //sets level of the skill of each tech group

  ///build the best techs element
  let bestTechs = techs.best.techs.map((t) => {
    return (
      <div className="mb-2">
        <span className="skillH">{t.value}</span>
        <div className="progress my-1">
          <div className="progress-bar bg-success" style={bestLevel}></div>
        </div>
      </div>
    );
  });

  //same as best only for seconed
  let seconedLevel = { width: techs.seconed.level + "%" };
  let seconedTechs = techs.seconed.techs.map((t) => {
    return (
      <div className="mb-2">
        <span className="skillH">{t.value}</span>
        <div className="progress my-1">
          <div className="progress-bar bg-primary" style={seconedLevel}></div>
        </div>
      </div>
    );
  });

  //sets rest of tecs string
  let restTechs = "";
  for (let i = 0; i < techs.rest.length; i++) {
    let x = " ";
    let y = ", ";
    if (restTechs == "") restTechs = restTechs + x + techs.rest[i].value;
    else restTechs = restTechs + y + techs.rest[i].value;
  }

  let ex; // short for experrience
  let tempForsort = expiriense;

  /// sort the array by dates
  tempForsort.sort((a, b) => {
    console.log(a);
    a = a.Sdate.split("-");
    b = b.Sdate.split("-");
    ////0-year , 1-mount, 2-day
    let aSum = parseInt(a[0]) * 365 + parseInt(a[1]) * 30 + parseInt(a[2]);
    let bSum = parseInt(b[0]) * 365 + parseInt(b[1]) * 30 + parseInt(b[2]);
    if (aSum > bSum) return -1;
    if (bSum > aSum) return 1;
    else return 0;
  });
  ex = tempForsort;

  //sets the expireence array of element
  ex = expiriense.map((element) => {
    return (
      <div
        className="timline-card timline-card-primary card shadow-sm"
        id="outCard"
      >
        <div className="card-body">
          <div class="h5 mb-1">
            {element.jobTitle}{" "}
            <span class="text-muted h6">at {element.employer}</span>
          </div>
          <div class="text-muted text-small mb-2">
            {element.Sdate} - {element.Edate}
          </div>
          <div className="workPar">
            <p>{element.description}</p>
          </div>
        </div>
      </div>
    );
  });

  let edj; //short for educaiton
  tempForsort = educaition;

  /// sort the array by dates
  tempForsort.sort((a, b) => {
    console.log(a);
    a = a.Sdate.split("-");
    b = b.Sdate.split("-");
    ////0-year , 1-mount, 2-day
    let aSum = parseInt(a[0]) * 365 + parseInt(a[1]) * 30 + parseInt(a[2]);
    let bSum = parseInt(b[0]) * 365 + parseInt(b[1]) * 30 + parseInt(b[2]);
    if (aSum > bSum) return -1;
    if (bSum > aSum) return 1;
    else return 0;
  });
  edj = tempForsort;

  //sets the educaition array of element
  edj = edj.map((element) => {
    return (
      <div
        className="timline-card timline-card-primary card shadow-sm"
        id="outCard2"
      >
        <div className="card-body">
          <div class="h5 mb-1">
            {element.degree}{" "}
            <span class="text-muted h6">from {element.school}</span>
          </div>
          <div class="text-muted text-small mb-2">
            {element.Sdate} - {element.Edate}
          </div>
          <div className="workPar">
            <p>{element.description}</p>
          </div>
        </div>
      </div>
    );
  });

  ////make sure the heading will not be printed if there is no value
  let educaitionExists = "";
  if (educaition.length > 0) {
    educaitionExists = "Education";
  }
  let workExists = "";
  if (ex.length > 0) {
    workExists = "Work Experience";
  }

  //  sets the amount of page needs to be render
  let amountOfpages = Math.ceil((ex.length + educaition.length) / 4);
  let pagesArr = [];
  let exCounter = 1;
  let edjcCounter = 1;

  //sets the ex and edj into array of arrays with lenght 4 for each
  //array unit so it will be fitted into pages
  for (let i = 0; i < amountOfpages; i++) {
    pagesArr[i] = [];
    for (let j = 0; j < 4; j++) {
      if (ex.length > 0) {
        if (exCounter == 1) {
          pagesArr[i].push(<h2 className="aboutHeader3">{workExists}</h2>); //pushs heading if its the first of a kind
          j--;
          exCounter = 0;
          continue;
        }
        pagesArr[i].push(ex[ex.length - 1]);
        ex.splice(ex.length - 1, 1);
      } else {
        if (edjcCounter == 1) {
          pagesArr[i].push(
            <h2 className="aboutHeader3">{educaitionExists}</h2> ////pushs heading if its the first of a kind
          );
          edjcCounter = 0;
          j--;
          continue;
        }

        if (edj.length > 0) {
          pagesArr[i].push(edj[edj.length - 1]);
          edj.splice(edj.length - 1, 1);
        }
      }
    }
  }

  //sets the pages as html elements
  let pages = [];
  for (let i = 0; i < amountOfpages; i++) {
    pages[i] = (
      <div className="page">
        <div className="experience">
          <div className="work1">
            <div className="timeLine">{pagesArr[i]}</div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <React.Fragment>
      <div id="book" className="book">
        <div id="page" className="page" style={{ marginTop: "0px" }}>
          <div className={pickedTamplate}>
            <img src={avatrImg} id="avatar"></img>
            <div className="headingControl">
              <h1 id="nameHeader">{fullName}</h1>
              <h4 id="profHeader">{personalInfo.wills}</h4>
            </div>
          </div>
          <div className="about">
            <div className="details">
              <div className="about2">
                <h2 className="aboutHeader">About Me</h2>
                <p className="par">{about}</p>
              </div>
              <div className="about2">
                <div class="row mt-2">
                  <div class="col-sm-4">
                    <div class="pb-1">Email</div>
                  </div>
                  <div class="col-sm-8">
                    <div class="pb-1 text-secondary">
                      {personalInfo.phoneNumber}
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="pb-1">Phone</div>
                  </div>
                  <div class="col-sm-8">
                    <div class="pb-1 text-secondary">{personalInfo.mail}</div>
                  </div>
                  <div class="col-sm-4">
                    <div class="pb-1">Address</div>
                  </div>
                  <div class="col-sm-8">
                    <div class="pb-1 text-secondary">
                      {personalInfo.address}
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="pb-1">Date of birth</div>
                  </div>
                  <div class="col-sm-8">
                    <div class="pb-1 text-secondary">{personalInfo.age}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="personalSkills">
            <h2 className="aboutHeader2">Professional Skills</h2>
            <div className="personalSkills-content">
              {bestTechs}
              {seconedTechs}
            </div>
            <p className="par2">
              <b>More technologies:</b> {restTechs}{" "}
            </p>
            <p className="par2">
              <b>Languages :</b> {languages}{" "}
            </p>
          </div>

          <div className="contact">
            <h2 className="aboutHeader4">
              LinkedIn{" "}
              <span id="linkdinLink" class="text-muted h6">
                {techs.links.linkdin}
              </span>
            </h2>
            <h2 className="aboutHeader4">
              Github{" "}
              <span id="gitLink" class="text-muted h6">
                {techs.links.gitHub}
              </span>
            </h2>
          </div>
        </div>
        {pages} {/* display all of the educaition and expirience pages */}
      </div>
    </React.Fragment>
  );
};

export default FinnalDisplay;
