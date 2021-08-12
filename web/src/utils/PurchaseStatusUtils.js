export const isOnStatus = (status, opportunity) => {
  if (opportunity && opportunity.status) {
    return opportunity.status === status;
  }
  return false;
};

export const isPurchaseOnStatus = (status, purchase) => {
  if (purchase && purchase.status) {
    return purchase.status === status;
  }
  return false;
};

export const purchasePriorityLevel = (priority) => {
  if (priority) {
    switch (Number(priority)) {
      case 1:
        return "success";
      case 2:
        return "warning";
      case 3:
        return "danger";
      default:
        priority;
    }
  }
};
