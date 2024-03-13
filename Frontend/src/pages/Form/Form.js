import React, { useEffect } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import Multiselect from "multiselect-react-dropdown";

export default function Form() {
  const {
    register,
    formState: { errors },
    handleSubmit,
    watch,
    setValue,
    getValues,
  } = useForm({ defaultValues: { country: [] } });

  const onSubmit = (data) => {
    // alert(JSON.stringify(data));
    alert(watch().marital_status);
  };
  useEffect(() => {
    const getcountrydata = async () => {
      const getcountryname = ["India", "US", "Japan", "UAE"];
      setValue("country", getcountryname);
    };
    getcountrydata();
  }, []);
  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <h1>Registration</h1>
        </div>
        <div>
          <label>Name</label>
          <input
            placeholder="Enter person name"
            {...register("name", { required: true })}
          />
          <error>
            {errors.name?.type === "required" && "Name is required"}
          </error>
        </div>
        <div>
          <label>Email</label>
          <input
            placeholder="Enter primary email"
            {...register("email", {
              required: true,
              pattern: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/i,
            })}
          />
          <error>
            {errors.email?.type === "required" && "Email is required"}
            {errors.email?.type === "pattern" &&
              "Entered email is in wrong format"}
          </error>
        </div>
        <div>
          <label>Phone Number</label>
          <input
            type="number"
            {...register("number", {
              minLength: 6,
              maxLength: 12,
            })}
          />
          <error>
            {errors.number?.type === "minLength" &&
              "Entered number is less than 6 digits"}
            {errors.number?.type === "maxLength" &&
              "Entered number is more than 12 digits"}
          </error>
        </div>
        <div>
          <label>Password</label>
          <input
            placeholder="Enter password"
            {...register("password", {
              required: true,
              minLength: 5,
              maxLength: 20,
            })}
          />
          <error>
            {errors.password?.type === "minLength" &&
              "Entered password is less than 5 characters"}
            {errors.password?.type === "maxLength" &&
              "Entered password is more than 20 characters"}
          </error>
        </div>
        <label>
          Department:
          <select {...register("department", { required: true })}>
            <option value="">Select Department</option>
            <option value="HR">HR</option>
            <option value="IT">IT</option>
            <option value="other">other</option>
          </select>
          <error>
            {errors.department?.type === "required" && "Invalid department"}
          </error>
        </label>
        {/* <label>
          Competence:
          <Multiselect
            isObject={false}
            onRemove={(event) => {
              console.log(event);
            }}
            onSelect={(event) => {
              console.log(event);
            }}
            options={{ ...register("country", { required: true }) }}
            showCheckbox
          />
        </label> */}
        <div>
          <label>
            Choose languages you know:
            <label htmlFor="c">C</label>
            <input
              type="checkbox"
              id="c"
              value="C"
              {...register("language", { required: true })}
              onChange={() => {}}
            />
            <label htmlFor="cpp">C++</label>
            <input
              type="checkbox"
              id="cpp"
              value="CPP"
              {...register("language", { required: true })}
              onChange={() => {}}
            />
            <label htmlFor="java">Java</label>
            <input
              type="checkbox"
              id="java"
              value="Java"
              {...register("language", { required: true })}
              onChange={() => {}}
            />
            <label htmlFor="python">Python</label>
            <input
              type="checkbox"
              id="python"
              value="Python"
              {...register("language", { required: true })}
              onChange={() => {}}
            />
            <error>
              {errors.language?.type === "required" &&
                "select alleast 1 language"}
            </error>
          </label>
        </div>
        <div>
          <label>
            Marital Status:
            <input
              {...register("marital_status", { required: true })}
              type="radio"
              id="agree"
              value="Yes"
              onChange={() => {}}
            />
            <label htmlFor="agree">Yes</label>
            <input
              type="radio"
              id="disagree"
              {...register("marital_status", { required: true })}
              value="No"
            />
            <label htmlFor="disagree">No</label>
            <error>
              {errors.marital_status?.type === "required" &&
                "marital_status not selected"}
            </error>
            Spouse Name:
            <input
              name="input"
              type="text"
              disabled={watch().marital_status === "Yes"}
              {...register("spouse_name")}
            />
          </label>
        </div>
        <div>
          <label>
            Do you agree with this statement?
            <input
              type="radio"
              // id="agree"
              value="Yes"
              {...register("agree")}
              // checked={agree === "Yes"}
              onChange={() => {}}
            />
            <label htmlFor="agree">Yes</label>
            <input
              type="radio"
              id="disagree"
              value="No"
              {...register("agree")}
              // checked={agree === "No"}
              onChange={() => {}}
            />
            <label htmlFor="disagree">No</label>
          </label>
        </div>

        <div>
          <input className="button" type="submit" />
        </div>
      </form>
      {/* <PaginatedItems itemsPerPage={4} items={[1, 2, 3, 4, 5]} /> */}
    </div>
  );
}
