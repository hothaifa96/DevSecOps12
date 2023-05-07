import { useForm } from "react-hook-form";
import Select from "react-select";
import { useNavigate } from "react-router-dom";

let options = [];
///data base for languages
let optionList = [
  "English",
  "Spanish",
  "French",
  "German",
  "Chinese",
  "Russian",
  "Japanese",
  "Arabic",
  "Italian",
  "Portuguese",
  "Dutch",
  "Swedish",
  "Polish",
  "Korean",
  "Turkish",
  "Finnish",
  "Indonesian",
  "Norwegian",
  "Greek",
  "Thai",
  "Irish",
  "Welsh",
  "Scots",
  "Scottish Gaelic",
  "Breton",
  "Cornish",
  "Irish Gaelic",
  "Manx",
  "Basque",
  "Luxembourgish",
  "Afrikaans",
  "Albanian",
  "Bosnian",
  "Macedonian",
  "Montenegrin",
  "Serbo-Croatian",
  "Croatian",
  "Serbian",
  "Bosnian",
  "Montenegrin",
  "Hindi",
  "Czech",
  "Hebrew",
  "Vietnamese",
  "Hungarian",
  "Ukrainian",
  "Slovak",
  "Bulgarian",
  "Croatian",
  "Lithuanian",
  "Estonian",
  "Serbian",
  "Latvian",
  "Catalan",
  "Slovenian",
  "Romanian",
  "Persian",
  "Tamil",
  "Malay",
  "Telugu",
];

//sets languages data into the object shaoe needed for a muilti select
options = optionList.map((e) => {
  return { value: e, label: e };
});

const PersonalInfo = (props) => {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    defaultValues: {
      wills: "",
      firstName: "",
      lastName: "",
      mail: "",
      phoneNumber: "",
      adress: "",
      age: "",
      gender: "",
    },
  });
  return (
    <div id="backround">
      <div id="container" className="shadow-sm p-3 mb-5 bg-body rounded">
        <form
          onSubmit={handleSubmit((data) => {
            props.handlePersonalInfo(data);
            reset();
            navigate("/about");
          })}
        >
          <h3 className="mb-2 mt-1 mt-2">Personal informaition</h3>
          <div class="form-control mb-3">
            <div class="form-group ">
              <label className="mb-2 mt-1 mt-2">wills</label>
              <input
                {...register("wills")}
                type="text"
                class="form-control"
                placeholder="My dream is to become.."
              ></input>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group ">
                  <label className="mb-2 mt-1 mt-2">First name</label>
                  <input
                    {...register("firstName", { required: "this is required" })}
                    type="text"
                    class="form-control"
                    placeholder="First name"
                  ></input>
                  <p>{errors.firstName?.message}</p>
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label className="mb-2 mt-1 mt-2">Last name</label>
                  <input
                    {...register("lastName", { required: "this is required" })}
                    type="text"
                    class="form-control"
                    placeholder="Last name"
                  ></input>
                  <p>{errors.lastName?.message}</p>
                </div>
              </div>
            </div>
          </div>

          <div class="form-control mb-3">
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label className="mb-2 mt-1 mt-2">Date of birth</label>
                  <input
                    {...register("age", { required: "this is required" })}
                    type="date"
                    class="form-control"
                    placeholder="17.04.1996"
                  ></input>
                  <p>{errors.age?.message}</p>
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label className="mb-2 mt-1 mt-2">Choose gender</label>
                  <select
                    {...register("gender", { required: "this is required" })}
                    class="form-select"
                    aria-label="Default select example"
                  >
                    <option value="male">male</option>
                    <option value="woman">female</option>
                    <option value="other">other</option>
                  </select>
                  <p>{errors.gender?.message}</p>
                </div>
              </div>
            </div>
          </div>

          {/* ///////////////////////////////////////////////////////////// */}
          <div class="form-control mb-3">
            <div class="form-group">
              <label className="mb-2 mt-1 mt-2">Email</label>
              <input
                {...register("phoneNumber", { required: "this is required" })}
                type="email"
                class="form-control"
                placeholder="example@example.com"
              ></input>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group ">
                  <label className="mb-2 mt-1 mt-2">Phone number</label>
                  <input
                    {...register("mail")}
                    type="text"
                    class="form-control"
                    id="inputCity"
                    placeholder="0523351768"
                  ></input>
                </div>
              </div>

              <div class="col">
                <div class="form-group ">
                  <label className="mb-2 mt-1 mt-2">Adress</label>
                  <input
                    {...register("adress")}
                    type="text"
                    class="form-control"
                    placeholder="104 central park st"
                  ></input>
                </div>
              </div>
            </div>
          </div>

          <div class="form-control">
            <label className="mb-2 mt-1 mt-2">Speaking language</label>
            <Select
              options={options}
              isMulti
              onChange={(seleced) => props.handlePersonalInfo_Multis(seleced)}
            />
          </div>

          <button type="submit" class="btn btn-dark mt-3">
            continue
          </button>
        </form>
      </div>
    </div>
  );
};

export default PersonalInfo;
