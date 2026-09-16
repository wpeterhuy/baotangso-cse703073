<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Scene extends Model
{
    protected $table = 'scenes';
    public $timestamps = true;
    const UPDATED_AT = null;

    protected $fillable = [
        'museum_id', 'title', 'slug', 'panorama_url', 'thumbnail_url',
        'initial_yaw', 'initial_pitch', 'initial_fov', 'audio_url',
        'order_index', 'status',
    ];

    protected $casts = [
        'initial_yaw' => 'decimal:3',
        'initial_pitch' => 'decimal:3',
        'initial_fov' => 'decimal:2',
    ];

    public function museum()
    {
        return $this->belongsTo(Museum::class);
    }

    public function viewpoints()
    {
        return $this->hasMany(Viewpoint::class);
    }

    public function hotspots()
    {
        return $this->hasMany(Hotspot::class)->orderBy('order_index');
    }

    public function tourSteps()
    {
        return $this->hasMany(TourStep::class);
    }
}
