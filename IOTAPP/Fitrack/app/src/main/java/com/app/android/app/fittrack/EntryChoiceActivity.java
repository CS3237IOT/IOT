/*
 * Copyright 2020 Google LLC. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.app.android.app.fittrack;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.app.android.app.fittrack.java.ChooserActivity;
import com.app.android.app.fittrack.java.LivePreviewActivity;
import com.google.firebase.FirebaseError;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public final class EntryChoiceActivity extends AppCompatActivity {


    FirebaseDatabase firebaseDatabase;
    public DatabaseReference currentActivity;
    public DatabaseReference dbSitupCount;
    public DatabaseReference dbJumpingCount;
    public DatabaseReference dbPushupCount;

    public DatabaseReference dbTemp;

    // variable for view items.
    private TextView tvHeatText;
    private TextView tvHeatdata;
    private TextView tvPredictedActivity;
    private TextView tvRepetition;
    private TextView tvTimes;
    private ImageView ivActivity;
    private static String[] COUNT_LIST = {"pushup_count","situp_count","jump_count"};
    private static String[] RISK_LEVEL = {"safe","attention","warning","dangerous","extremely dangerous"};

    ArrayList<String> arrayList = new ArrayList<>();
    ArrayAdapter<String> arrayAdapter;

    SimpleDateFormat date = new SimpleDateFormat("yyyy-MM-dd");
    String today = date.format(new Date());

    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.setContentView(R.layout.activity_vision_entry_choice);
        ImageButton startPosture = findViewById(R.id.ibPosture);

        startPosture.setOnClickListener((View.OnClickListener)(new View.OnClickListener() {
            public final void onClick(View it) {
            Intent intent = new Intent((Context)EntryChoiceActivity.this, LivePreviewActivity.class);
            EntryChoiceActivity.this.startActivity(intent);
        }
    }));

        tvHeatText = findViewById(R.id.tvHeatText);
        tvHeatdata = findViewById(R.id.tvHeatdata);
        tvPredictedActivity = findViewById(R.id.tvPredictedActivity);
        tvRepetition = findViewById(R.id.tvRepetition);
        ivActivity = findViewById(R.id.ivActivity);
        tvTimes = findViewById(R.id.tvTimes);

        firebaseDatabase = FirebaseDatabase.getInstance();
        DatabaseReference rootRef = FirebaseDatabase.getInstance().getReference();

        rootRef.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                if (snapshot.hasChild("date"+"/"+today)) {
                    getdisplayData();
                    getdata();
                }else{
                    DatabaseReference ref = FirebaseDatabase.getInstance().getReference();
                    DatabaseReference usersRef = ref.child("date");
                    usermodel User = new usermodel(0,0,0,"idle","T: 23.22C H: 60.44% Feels: 25.31C");
                    usersRef.child(today).setValue(User);
                    getdisplayData();
                    getdata();
                }
            }
            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        firebaseDatabase = FirebaseDatabase.getInstance();
        DatabaseReference databaseReference = firebaseDatabase.getReference("date");
        ListView listView = findViewById(R.id.simpleListView);
        databaseReference.addChildEventListener(new ChildEventListener() {
            @Override
            public void onChildAdded(DataSnapshot dataSnapshot, String s) {
                usermodel user = (usermodel) dataSnapshot.getValue(usermodel.class);
                String userString = String.valueOf(user);
                arrayList.add(dataSnapshot.getKey() + "\n"+userString);
                ArrayList<String> tmpArr = new ArrayList<>(arrayList);
                Collections.reverse(tmpArr);
                arrayAdapter = new ArrayAdapter<>(EntryChoiceActivity.this , R.layout.list_item , tmpArr);
                listView.setAdapter(arrayAdapter);
        }
        @Override
        public void onChildChanged(DataSnapshot dataSnapshot, String s) {
            arrayList.remove(arrayList.size()-1);
            usermodel user = (usermodel) dataSnapshot.getValue(usermodel.class);
            String userString = String.valueOf(user);
            System.out.println(userString);
            arrayList.add(dataSnapshot.getKey() + "\n"+userString);
            ArrayList<String> tmpArr = new ArrayList<>(arrayList);
            Collections.reverse(tmpArr);
            arrayAdapter = new ArrayAdapter<>(EntryChoiceActivity.this , R.layout.list_item , tmpArr);
            listView.setAdapter(arrayAdapter);

            }


        @Override
        public void onChildRemoved(DataSnapshot dataSnapshot) {

        }
        @Override
        public void onChildMoved(DataSnapshot dataSnapshot, String s) {

        }
       @Override
       public void onCancelled(DatabaseError databaseError) {

        }
        });
    }


    public void getdisplayData() {
        currentActivity = firebaseDatabase.getReference("date" + "/" + today + "/message");       //.getReference("message");
        dbPushupCount = firebaseDatabase.getReference("date" + "/" + today + "/pushup_count");
        dbSitupCount = firebaseDatabase.getReference("date" + "/" + today + "/situp_count");
        dbJumpingCount = firebaseDatabase.getReference("date" + "/" + today + "/jump_count");
        dbTemp = firebaseDatabase.getReference("date" + "/" + today + "/temp");

    }

    private void getdata() {
        // calling add value event listener method
        // for getting the values from database.
        currentActivity.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    // this method is call to get the realtime
                    // updates in the data.
                    // this method is called when the data is
                    // changed in our Firebase console.
                    // below line is for getting the data from
                    // snapshot of our database.
                    String value = snapshot.getValue(String.class);
                    // after getting the value we are setting
                    // our value to our text view in below line.
                    tvPredictedActivity.setText(value);
                    switch (Objects.requireNonNull(value)) {
                        case "idle":
                            ivActivity.setImageResource(R.drawable.idle);
                            tvRepetition.setText(" ");
                            tvTimes.setText(" ");
                            break;
                        case "walking":
                            ivActivity.setImageResource(R.drawable.walk);
                            tvRepetition.setText(" ");
                            tvTimes.setText(" ");
                            break;
                        case "running":
                            ivActivity.setImageResource(R.drawable.run);
                            tvRepetition.setText(" ");
                            tvTimes.setText(" ");
                            break;

                        case "push-up":
                            ivActivity.setImageResource(R.drawable.pushup);
                            dbPushupCount.addValueEventListener(new ValueEventListener() {
                                @Override
                                public void onDataChange(@NonNull DataSnapshot snapshot) {
                                    // this method is call to get the realtime
                                    // updates in the data.
                                    // this method is called when the data is
                                    // changed in our Firebase console.
                                    // below line is for getting the data from
                                    // snapshot of our database.
                                    Integer value = snapshot.getValue(Integer.class);
                                    String textvalue =  String.valueOf(value);
                                    // after getting the value we are setting
                                    // our value to our text view in below line.
                                    tvRepetition.setText(textvalue);
                                    tvTimes.setText(" Times");
                                }
                                @Override
                                public void onCancelled(@NonNull DatabaseError error) {
                                    Toast.makeText(EntryChoiceActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
                                }
                            });
                            break;

                        case "sit-up":
                            ivActivity.setImageResource(R.drawable.situp);
                            dbSitupCount.addValueEventListener(new ValueEventListener() {
                                @Override
                                public void onDataChange(@NonNull DataSnapshot snapshot) {
                                    // this method is call to get the realtime
                                    // updates in the data.
                                    // this method is called when the data is
                                    // changed in our Firebase console.
                                    // below line is for getting the data from
                                    // snapshot of our database.
                                    Integer value = snapshot.getValue(Integer.class);
                                    String textvalue =  String.valueOf(value);
                                    // after getting the value we are setting
                                    // our value to our text view in below line.
                                    tvRepetition.setText(textvalue);
                                    tvTimes.setText(" Times");
                                }
                                @Override
                                public void onCancelled(@NonNull DatabaseError error) {
                                    Toast.makeText(EntryChoiceActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
                                }
                            });
                            break;

                        case "jumping jack":
                            ivActivity.setImageResource(R.drawable.jump);
                            dbJumpingCount.addValueEventListener(new ValueEventListener() {
                                @Override
                                public void onDataChange(@NonNull DataSnapshot snapshot) {
                                    // this method is call to get the realtime
                                    // updates in the data.
                                    // this method is called when the data is
                                    // changed in our Firebase console.
                                    // below line is for getting the data from
                                    // snapshot of our database.
                                    Integer value = snapshot.getValue(Integer.class);
                                    String textvalue =  String.valueOf(value);
                                    // after getting the value we are setting
                                    // our value to our text view in below line.
                                    tvRepetition.setText(textvalue);
                                    tvTimes.setText(" Times");
                                }
                                @Override
                                public void onCancelled(@NonNull DatabaseError error) {
                                    Toast.makeText(EntryChoiceActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
                                }
                            });
                            break;
                        default:
                            ivActivity.setImageResource(R.drawable.idle);
                            break;
                    }
                }
                @Override
                public void onCancelled(@NonNull DatabaseError error) {
                    Toast.makeText(EntryChoiceActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
                }
            });

        dbTemp.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String value = snapshot.getValue(String.class);
                tvHeatdata.setText(value);
                int len = value.length()-1;
                String substr = value.substring(len-5, len-1);
                Float temp = Float.parseFloat(substr);
                LinearLayout li =(LinearLayout)findViewById(R.id.layoutid);

                if (temp>52.2) {
                    tvHeatText.setText("Extremely Dangerous");
                    li.setBackgroundColor(Color.parseColor("#ff0000"));
                }
                else if (temp>39.4) {
                    tvHeatText.setText("Dangerous");
                    li.setBackgroundColor(Color.parseColor("#ff4c4c"));
                }
                else if (temp>32.8) {
                    tvHeatText.setText("Warning");
                    li.setBackgroundColor(Color.parseColor("#FFA500"));
                }
                else if (temp>26.7) {
                    tvHeatText.setText("Attention");
                    li.setBackgroundColor(Color.parseColor("#FFC55C"));
                }
                else {
                    tvHeatText.setText("Safe");
                    li.setBackgroundColor(Color.parseColor("#4286f4"));
                }

            }
            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

  }

}


