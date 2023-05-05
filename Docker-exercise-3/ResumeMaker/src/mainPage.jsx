import React, { Component } from "react";
import { Routes, Route, Link } from "react-router-dom";
//style import
import "../src/components/style.css";
import printIcon from "./images/printIcon.png";
//pdf import
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

//components import
import About from "./components/about";
import PersonalInfo from "./components/personalInfo";
import Experience from "./components/experience";
import Educaition from "./components/educaition";
import Techs from "./components/techs";
import Inderdoction from "./components/interdoction";
import FinnalDisplay from "./components/finalDisplay";
import BgOption from "./components/tamplatePick";

export default class Main extends Component {
  state = {
    resume: {
      personalInfo: {
        wills: "",
        firstName: "",
        lastName: "",
        mail: "",
        phoneNumber: "",
        Language: [],
        age: "",
        address: "",
        gender: "",
      },
      about: "",
      expiriense: [],
      educaition: [],
      techs: {
        best: {
          techs: [],
          level: "",
        },
        seconed: {
          techs: [],
          level: "",
        },
        rest: [],

        links: {
          linkdin: "",
          gitHub: "",
        },
      },
      tamplate: "1",
    },
  };

  render() {
    return (
      <body className="text-center text-bg-dark">
        <div className="container23">
          <div id="row1">
            <div className="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
              <header className="mb-auto">
                <div>
                <h3 className="float-md-start mb-0">
                    <Link
                      style={{ color: "white", textDecoration: "none" }}
                      to="/"
                    >
                      ResuMaker
                    </Link>
                  </h3>
                  <nav className="nav nav-masthead justify-content-center float-md-end">
                    <a
                      className="nav-link fw-bold py-1 px-0 active"
                      aria-current="page"
                      href="#"
                    >
                      Home
                    </a>
                    <a className="nav-link fw-bold py-1 px-0" href="#">
                      Features
                    </a>
                    <img
                      onClick={this.printHtml}
                      id="printIcon"
                      src={printIcon}
                      alt="arr"
                    />
                  </nav>
                </div>
              </header>
            </div>
          </div>

          <div className="row2">
            <Routes>
              <Route path="/" element={<Inderdoction />} />
              <Route
                path="/tamplate"
                element={
                  <BgOption handleTamplate={(e) => this.handleTamplate(e)} />
                }
              />
              <Route
                path="/personal"
                element={
                  <PersonalInfo
                    handlePersonalInfo={(personalInfo) =>
                      this.handlePersonalInfo(personalInfo)
                    }
                    handlePersonalInfo_Multis={(selectedOptions) =>
                      this.handlePersonalInfo_Multis(selectedOptions)
                    }
                  />
                }
              />
              <Route
                path="/about"
                element={
                  <About
                    handleAbout={(aboutInfo) => this.handleAbout(aboutInfo)}
                  />
                }
              />
              <Route
                path="/ex"
                element={
                  <Experience handleXP={(xpArr) => this.handleXP(xpArr)} />
                }
              />
              <Route
                path="/educaition"
                element={
                  <Educaition
                    handleEducaition={(educaitionInfo) =>
                      this.handleEducaition(educaitionInfo)
                    }
                  />
                }
              />
              <Route
                path="/techs"
                element={
                  <Techs
                    handleLinks={(links) => this.handleLinks(links)}
                    handleBesttechs={(picks) => {
                      this.handleBesttechs(picks);
                    }}
                    handleSeconedtechs={(picks) => {
                      this.handleSeconedtechs(picks);
                    }}
                    handleRestofTechs={(picks) => {
                      this.handleRestofTechs(picks);
                    }}
                    pickedMain={this.state.resume.techs.best.techs.length} //alow to contol the limit on selected languges
                    pickedSec={this.state.resume.techs.seconed.techs.length} //alow to contol the limit on selected languges
                  />
                }
              />
            </Routes>
            <FinnalDisplay resume={this.state.resume} />
          </div>
        </div>
      </body>
    );
  }

  /// prints the pdf///
  printHtml = () => {
    let gitLink = this.state.resume.techs.links.gitHub;
    let linkdinLink = this.state.resume.techs.links.linkdin;
    let data = document.getElementById("book"); // element to print
    let canvas = document.createElement("canvas");
    let highetWorking = //to count how many pages and set the hight of the pdf
      (1 +
        Math.ceil(
          (this.state.resume.expiriense.length +
            this.state.resume.educaition.length) /
            4
        )) *
      1160;

    canvas.width = 795;
    canvas.height = highetWorking;

    var options = {
      canvas: canvas,
      scale: 1,
      width: 1920,
      height: 1280,
      windowHeight: 1280,
      windowWidth: 1920,
    };

    html2canvas(data, options).then((canvas) => {
      const contentDataURL = canvas.toDataURL("image/png");
      var pdf = new jsPDF("p", "px", [highetWorking, 795]);

      var width = pdf.internal.pageSize.getWidth();
      var height = pdf.internal.pageSize.getHeight();

      pdf.addImage(contentDataURL, "PNG", 1, 1, width, height);
      //hyper links
      pdf.link(170, 930, 280, 40, { url: linkdinLink.toString() });
      pdf.link(170, 1030, 280, 40, { url: gitLink.toString() });
      pdf.save("ResuMaker");
    });
  };

  /// changes back round picture from the div class name using tamplate
  handleTamplate = (e) => {
    let resume = this.state.resume;
    if (typeof e.target.className[13] == "string") {
      resume.tamplate = e.target.className[12] + e.target.className[13];
      console.log(resume.tamplate);
    } else {
      resume.tamplate = e.target.className[12];
    }
    this.setState({ resume });
  };

  //handle about form
  handleAbout = (aboutInfo) => {
    let resume = this.state.resume;
    resume.about = aboutInfo.about;
    this.setState({ resume });
  };

  ////both for personal info//////////////
  /// handle most of the info
  handlePersonalInfo = (personalInfo) => {
    let resume = this.state.resume;
    resume.personalInfo.firstName = personalInfo.firstName;
    resume.personalInfo.lastName = personalInfo.lastName;
    resume.personalInfo.mail = personalInfo.mail;
    resume.personalInfo.phoneNumber = personalInfo.phoneNumber;
    resume.personalInfo.wills = personalInfo.wills;
    resume.personalInfo.address = personalInfo.adress;
    resume.personalInfo.age = personalInfo.age;
    resume.personalInfo.gender = personalInfo.gender;
    this.setState({ resume });
  };

  /// handl only the multi select for languges
  handlePersonalInfo_Multis = (selectedOptions) => {
    let resume = this.state.resume;
    resume.personalInfo.Language = selectedOptions.map((e) => e.value);

    this.setState({ resume });
  };
  ///////////////////////////////////////

  /// handle all the expirience form
  handleXP = (xpArr) => {
    let resume = this.state.resume;
    resume.expiriense.push(xpArr);
    this.setState({ resume });
  };

  // handle educaitiopn form
  handleEducaition = (educaitionInfo) => {
    let resume = this.state.resume;
    resume.educaition.push(educaitionInfo);
    this.setState({ resume });
  };

  ////both for techs//////////////
  handleBesttechs = (picks) => {
    let resume = this.state.resume;
    resume.techs.best.techs = picks;
    this.setState({ resume });
  };

  handleSeconedtechs = (picks) => {
    let resume = this.state.resume;
    resume.techs.seconed.techs = picks;
    this.setState({ resume });
  };

  handleRestofTechs = (picks) => {
    let resume = this.state.resume;
    resume.techs.rest = picks;
    this.setState({ resume });
  };

  handleLinks = (links) => {
    let resume = this.state.resume;
    resume.techs.best.level = links.best;
    resume.techs.seconed.level = links.seconed;
    resume.techs.links.linkdin = links.linkdinLink;
    resume.techs.links.gitHub = links.githubLink;

    this.setState({ resume });
  };
  ///////////////////////////////
}
