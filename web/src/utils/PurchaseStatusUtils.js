export const isOnStatus = (status, opportunity) => {
  if (opportunity && opportunity.status) {
    return opportunity.status === status;
  }
  return false;
};
