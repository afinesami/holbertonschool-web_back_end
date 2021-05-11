import { createUser, uploadPhoto } from './utils';

const asyncUploadUser = async () => {
  let result = {
    photo: null,
    user: null,
  };

  try {
    result = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
    return result;
  } catch (error) {
    return result;
  }
};

export default asyncUploadUser;
