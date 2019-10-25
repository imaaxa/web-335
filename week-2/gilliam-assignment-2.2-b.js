{
  invoice {
    _id
    date_created
    date_shipped
    subtotal
    tax
    total

    customer {
      _id
      first_name
      last_name
      date_of_birth
      user_name
    },

    line_item [
      {
        _id
        name
        price
        quantity
      },
      {
        _id
        name
        price
        quantity
      }
    ]
  }
}
