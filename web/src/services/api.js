import axios from "axios";

const PARTNER_TYPE_RESOURCE = "/partner-type/";
const PARTNER_RESOURCE = "/partner/";
const PRODUCT_CATEGORY_RESOURCE = "/product-category/";
const PRODUCT_RESOURCE = "/product/";
const PURCHASE_OPPORTUNITY_RESOURCE = "/purchase-opportunity/";
const PURCHASE_RESOURCE = "/purchase/";
const PAYMENT_RESOURCE = "/payment/";
const PAYMENT_MODE_RESOURCE = "/payment-mode/";

export const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 1000,
});

/** Product Category */

export const ProductCategoryService = {
  getAll() {
    return client.get(`${PRODUCT_CATEGORY_RESOURCE}`).catch((error) => {
      throw new Error(`ProductCategoryService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PRODUCT_CATEGORY_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`ProductCategoryService ${error}`);
    });
  },
};

/** Product */

export const ProductService = {
  find(filters) {
    return client
      .get(`${PRODUCT_RESOURCE}find?search=${filters}`)
      .catch((error) => {
        throw new Error(`ProductService ${error}`);
      });
  },

  all() {
    return client.get(`${PRODUCT_RESOURCE}`).catch((error) => {
      throw new Error(`ProductService ${error}`);
    });
  },

  allByCategory(category) {
    const PRODUCT_URL_FILTER = category
      ? `${PRODUCT_RESOURCE}category/find?category=${category}`
      : `${PRODUCT_RESOURCE}category/find`;

    return client.get(`${PRODUCT_URL_FILTER}`).catch((error) => {
      throw new Error(`ProductService ${error}`);
    });
  },
};

/** Partner */

export const PartnerService = {
  getAll() {
    return client.get(`${PARTNER_RESOURCE}`).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  genders() {
    return client.get(`${PARTNER_RESOURCE}genders`).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PARTNER_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  allByPartnerType(partnerTypeId) {
    return client
      .get(`${PARTNER_RESOURCE}partner-type/${partnerTypeId}`)
      .catch((error) => {
        throw new Error(`PartnerService ${error}`);
      });
  },

  create(partner) {
    return client.post(`${PARTNER_RESOURCE}`, partner).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  find(filters) {
    return client
      .get(`${PARTNER_RESOURCE}find?search=${filters}`)
      .catch((error) => {
        throw new Error(`PartnerService ${error}`);
      });
  },
};

/** Partner Type*/

export const PartnerTypeService = {
  getAll() {
    return client.get(`${PARTNER_TYPE_RESOURCE}`).catch((error) => {
      throw new Error(`PartnerTypeService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PARTNER_TYPE_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`PartnerTypeService ${error}`);
    });
  },
};

/** Purchase Opportunity */

export const PurchaseOpportunityService = {
  getAll(params) {
    if (params) {
      return client
        .get(`${PURCHASE_OPPORTUNITY_RESOURCE}`, { params })
        .catch((error) => {
          throw new Error(`PurchaseOpportunityService ${error}`);
        });
    }
    return client.get(`${PURCHASE_OPPORTUNITY_RESOURCE}`).catch((error) => {
      throw new Error(`PurchaseOpportunityService ${error}`);
    });
  },

  byId(id) {
    return client
      .get(`${PURCHASE_OPPORTUNITY_RESOURCE}${id}`)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },

  getAllStatus() {
    return client
      .get(`${PURCHASE_OPPORTUNITY_RESOURCE}status/all`)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },

  create(purchaseOpportunity) {
    return client
      .post(`${PURCHASE_OPPORTUNITY_RESOURCE}`, purchaseOpportunity)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },

  convertToPurchase(id) {
    return client
      .post(`${PURCHASE_OPPORTUNITY_RESOURCE}${id}/convert/purchase`)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },
};

/** Purchase */

export const PurchaseService = {
  all() {
    return client.get(`${PURCHASE_RESOURCE}`).catch((error) => {
      throw new Error(`PurchaseService ${error}`);
    });
  },

  allByPage(page) {
    return client.get(`${PURCHASE_RESOURCE}?page=${page}`).catch((error) => {
      throw new Error(`PurchaseService ${error}`);
    });
  },

  allByPartner(partner_id) {
    return client
      .get(`${PURCHASE_RESOURCE}partner/${partner_id}`)
      .catch((error) => {
        throw new Error(`PurchaseService ${error}`);
      });
  },
};

/** Payment */

export const PaymentService = {
  all(limit, offset) {
    return client
      .get(`${PAYMENT_RESOURCE}?limit=${limit}&offset=${offset}`)
      .catch((error) => {
        throw new Error(`PaymentService ${error}`);
      });
  },

  create(payment) {
    return client.post(`${PAYMENT_RESOURCE}`, payment).catch((error) => {
      throw new Error(`PaymentService ${error}`);
    });
  },
};

export const PaymentModeService = {
  all() {
    return client.get(`${PAYMENT_MODE_RESOURCE}`).catch((error) => {
      throw new Error(`PaymentModeService ${error}`);
    });
  },
};
