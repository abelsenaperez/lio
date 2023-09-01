{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyM36xsz+DP3K3i+23vx6Pjq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/abelsenaperez/lio/blob/master/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kEqxAQCHabJB"
      },
      "outputs": [],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pip"
      ],
      "metadata": {
        "id": "iqDMeq42eGSS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "MIkBfFEHameG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('que hay de ti')"
      ],
      "metadata": {
        "id": "aNna53ngarHK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.write"
      ],
      "metadata": {
        "id": "bxVTRSsohrKh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "x = st.slider(\"Select a value\")\n",
        "st.write(x, \"squared is\", x * x)"
      ],
      "metadata": {
        "id": "cd_p5JGBh0Hz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "streamlit run streamlit_app.py"
      ],
      "metadata": {
        "id": "SCM1LSs3h810"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "peLdSShmiFL6"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}