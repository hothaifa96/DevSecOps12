import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

const About = (props) => {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors }, //used to display arror on required fileds
    reset,
  } = useForm({
    defaultValues: {
      about: "",
    },
  });

  return (
    <div id="container" className="shadow-sm p-3 mt-3 mb-5 bg-body rounded">
      <form
        onSubmit={handleSubmit((data) => {
          props.handleAbout(data);
          reset();
          navigate("/techs");
        })}
      >
        <div className="form-group">
          <h3>Tell us about your self</h3>
          <p>for best chances of getting ypur dream job we recomned using</p>
          <p>
            a 50-100 words paragragh, and right details that are not included{" "}
          </p>
          <textarea
            {...register("about", { required: "this is required" })}
            className="form-control"
            rows="5"
            placeholder="tell us about your life story , the recomended amout of wards is not more than 100!"
          ></textarea>
          <p style={{ marginTop: "5px" }}>{errors.about?.message}</p>
        </div>
        <button type="submit" className="btn btn-dark mt-2">
          continue
        </button>
      </form>
    </div>
  );
};

export default About;
