import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

// bolean variable that helps me control if the
//user want to add another form or to sent him to the next page
let wereTogo = false;

const Educaition = (props) => {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors }, //to print error message
    reset,
  } = useForm({
    defaultValues: {
      school: "",
      degree: "",
      filed: "",
      Sdate: "", // start date
      Edate: "", // end date
      description: "",
    },
  });

  return (
    <div id="container" className="shadow-sm p-3  bg-body rounded">
      <form
        onSubmit={handleSubmit((data) => {
          props.handleEducaition(data);
          reset();
          // this is the function that desides were to send the user
          if (wereTogo) {
            wereTogo = !wereTogo;
            navigate("/educaition");
          } else navigate("/final");
        })}
      >
        <h3 className="mb-4 mt-1 mt-1">Education</h3>
        {/* print scholl name input and lable */}
        <div class="form-control">
          <div class="row">
            <div class="col">
              <div className="form-group">
                <label>School Name</label>
                <input
                  {...register("school", { required: "this is required" })}
                  className="form-control"
                  type="text"
                  placeholder="e.g Ironi H Tel Aviv"
                ></input>
                <p>{errors.school?.message}</p>
              </div>
            </div>

            {/* print degree name input and lable */}
            <div class="col">
              <div className="form-group">
                <label>Degree</label>
                <input
                  {...register("degree", { required: "this is required" })}
                  className="form-control"
                  type="text"
                  placeholder="e.g B.A in computer sience "
                ></input>
                <p>{errors.degree?.message}</p>
              </div>
            </div>
          </div>
        </div>

        {/* print start date name input and lable */}
        <div class="form-control mt-1">
          <div class="row">
            <div class="col">
              <div className="form-group">
                <label>Start Date</label>
                <input
                  {...register("Sdate")}
                  className="form-control"
                  type="date"
                ></input>
              </div>
            </div>

            {/* print end date name input and lable */}
            <div class="col">
              <div className="form-group">
                <label>End Date</label>
                <input
                  {...register("Edate")}
                  className="form-control"
                  type="date"
                ></input>
              </div>
            </div>
          </div>
        </div>

        {/* print textboxvfv name input and lable */}
        <div class="form-control mt-1">
          <div className="form-group ">
            <label>Describe</label>
            <textarea
              {...register("description", { required: "this is required" })}
              className="form-control"
              rows="5"
              placeholder="Give us some informaition about your achivments"
            ></textarea>
            <p>{errors.description?.message}</p>
          </div>
        </div>

        {/* this button cahnge the path to come back to the same form  */}
        <button onClick={() => changepath()} className="btn btn-dark mt-2 me-3">
          add another
        </button>
        <button type="submit" className="btn btn-dark mt-2">
          continue
        </button>
      </form>
    </div>
  );
};

let changepath = () => {
  wereTogo = true;
};

export default Educaition;
