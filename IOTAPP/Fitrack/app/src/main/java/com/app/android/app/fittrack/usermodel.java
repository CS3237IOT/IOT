package com.app.android.app.fittrack;

import androidx.annotation.Keep;

@Keep
public class usermodel {


    public Integer pushup_count,jump_count,situp_count;
    public String message, temp;


    public usermodel(Integer pushup_count, Integer jump_count, Integer situp_count, String message, String temp
                     ) {
        this.pushup_count = pushup_count;
        this.jump_count = jump_count;
        this.situp_count = situp_count;
        this.message = message;
        this.temp = temp;
    }

    public usermodel() {
    }

    public Integer getPushup_count() {
        return pushup_count;
    }

    public void setPushup_count(Integer pushup_count) {
        this.pushup_count = pushup_count;
    }

    public Integer getJump_count() {
        return jump_count;
    }

    public void setJump_count(Integer jump_count) {
        this.jump_count = jump_count;
    }

    public Integer getSitup_count() {
        return situp_count;
    }

    public void setSitup_count(Integer situp_count) {
        this.situp_count = situp_count;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }

    @Override
    public String toString() {
        return "Push-up: " + this.pushup_count.toString() + "\n" + "Sit-up: " + this.situp_count.toString()+ "\n" +
        "Jumping-jack: " + this.jump_count.toString();
    }
}

