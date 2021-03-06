$('#form_vehiculo_nuevo').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            codigo: {
                validators: {
                    notEmpty: {
                        message: 'El codigo del vehículo es requerido'
                    }
                }
            },
            cilindraje: {
                validators: {
                    notEmpty: {
                        message: 'El cilindraje del vehículo es requerido'
                    }
                }
            },
            marca: {
                validators: {
                    notEmpty: {
                        message: 'La marca del vehículo es requerida'
                    }

                }
            },

            linea: {
                validators: {
                    notEmpty: {
                        message: 'La linea del vehículo es requerida'
                    }

                }

            },

            modelo: {
                validators: {
                    notEmpty: {
                        message: 'El modelo del vehículo es requerido'
                    }

                }

            },

            tipo_combustible: {
                validators: {
                    notEmpty: {
                        message: 'El tipo de combustible del vehículo es requerido'
                    }

                }

            },

            color: {
                validators: {
                    notEmpty: {
                        message: 'El color del vehículo es requerido'
                    }

                }

            },
            fecha_ingreso:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar la fecha de ingreso del vehículo'
                    },
                    date: {
                        format: 'YYYY-MM-DD',
                        message: 'La fecha no es válida'
                    }

                }
            },

            valor: {
                validators: {
                    notEmpty: {
                        message: 'El valor del vehículo es requerido'
                    },
                    between: {
                            min: 0.0,
                            max: 2147483647,
                            message: 'El valor del vehículo debe ser menor a 2\'147.483.647'
                    }

                }

            }
        }
});


$('#form_vehiculo_usado').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            placa: {
                validators: {
                    notEmpty: {
                        message: 'La placa del vehículo es requerida'
                    },
                    stringLength: {
                        min: 5,
                        max: 6,
                        message: 'La placa del vehículo debe ser de 5 a 6 caracteres'
                    }
                }
            },
            cilindraje: {
                validators: {
                    notEmpty: {
                        message: 'El cilindraje del vehículo es requerido'
                    }
                }
            },
            marca: {
                validators: {
                    notEmpty: {
                        message: 'La marca del vehículo es requerida'
                    }

                }
            },

            linea: {
                validators: {
                    notEmpty: {
                        message: 'La linea del vehículo es requerida'
                    }

                }

            },

            modelo: {
                validators: {
                    notEmpty: {
                        message: 'El modelo del vehículo es requerido'
                    }

                }

            },

            tipo_combustible: {
                validators: {
                    notEmpty: {
                        message: 'El tipo de combustible del vehículo es requerido'
                    }

                }

            },

            color: {
                validators: {
                    notEmpty: {
                        message: 'El color del vehículo es requerido'
                    }

                }

            },

            servicio: {
                validators: {
                    notEmpty: {
                        message: 'El servicio del vehículo es requerido'
                    }

                }

            }
        }
});




