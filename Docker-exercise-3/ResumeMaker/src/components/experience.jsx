import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

let wereTogo = false;

const Experience = (props) => {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    defaultValues: {
      jobTitle: "",
      employer: "",
      Sdate: "", //start date
      Edate: "", //end date
      description: "",
    },
  });

  return (
    <div id="container" className="shadow-sm p-3 bg-body rounded">
      <form
        onSubmit={handleSubmit((data) => {
          props.handleXP(data);
          reset();
          if (wereTogo == true) {
            wereTogo = !wereTogo;
            navigate("/ex");
          } else navigate("/educaition");
        })}
      >
        <h3 className="mb-4 mt-1 mt-1">Work Expirience</h3>

        {/* job tilte */}
        <div class="row">
          <div class="col">
            <div className="form-group">
              <label>Job title</label>
              <input
                {...register("jobTitle", { required: "this is required" })}
                className="form-control"
                type="text"
                placeholder="e.g Full stack developer"
              ></input>
              <p>{errors.jobTitle?.message}</p>
            </div>
          </div>

          {/*Employer */}
          <div class="col">
            <div className="form-group">
              <label>Employer</label>
              <input
                {...register("employer", { required: "this is required" })}
                className="form-control"
                type="text"
                placeholder="e.g Microsoft co."
              ></input>
              <p>{errors.employer?.message}</p>
            </div>
          </div>
        </div>

        {/*start date */}
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

          {/*end date */}
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

        {/*description */}
        <div className="form-group mt-4">
          <label>Describe</label>
          <textarea
            {...register("description", { required: "this is required" })}
            className="form-control"
            rows="6"
            placeholder="we recommend using no more that 80 words and you cant pass 250 latters"
            maxlength="250"
          ></textarea>
          <p>{errors.description?.message}</p>
        </div>

        {/*cahnges path and submit */}
        <button onClick={() => changepath()} className="btn btn-dark mt-2 me-3">
          add another
        </button>

        {/*only submit */}
        <button type="submit" className="btn btn-dark mt-2">
          next
        </button>
      </form>
    </div>
  );
};
//helps control the path
let changepath = () => {
  wereTogo = !wereTogo;
};

export default Experience;
