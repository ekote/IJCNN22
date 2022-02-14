# (..)
parameter_space = {
    "model": choice(
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet18_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet50_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(15),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(30),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("sgd"),
            "learning_rate": choice(0.001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adam"),
            "learning_rate": choice(0.00001),
        },
        {
            "model_name": choice("maskrcnn_resnet152_fpn"),
            "number_of_epochs": choice(50),
            "optimizer": choice("adamw"),
            "learning_rate": choice(0.00001),
        },
    ),
}

tuning_settings = {
    "iterations": 27,
    "max_concurrent_iterations": 27,
    "hyperparameter_sampling": RandomParameterSampling(parameter_space),
}
