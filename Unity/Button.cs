﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Button : MonoBehaviour
{

    public bool quit;

    public string name;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void button(){
        if(quit) UnityEngine.Application.Quit();
        else SceneManager.LoadScene(name);
    }
}
