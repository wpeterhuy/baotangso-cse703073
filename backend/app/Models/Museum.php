<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Museum extends Model
{
    use HasFactory;

    protected $table = 'museums';
    public $timestamps = true;
    const UPDATED_AT = null;

    protected $fillable = [
        'name', 'slug', 'address', 'lat', 'lng',
        'description', 'cover_image', 'opening_hours', 'status',
    ];

    protected $casts = [
        'opening_hours' => 'array',
        'lat' => 'decimal:7',
        'lng' => 'decimal:7',
    ];

    public function scenes()
    {
        return $this->hasMany(Scene::class)->orderBy('order_index');
    }

    public function artifacts()
    {
        return $this->hasMany(Artifact::class);
    }

    public function tours()
    {
        return $this->hasMany(Tour::class);
    }

    public function visitSessions()
    {
        return $this->hasMany(VisitSession::class);
    }

    public function guestbookEntries()
    {
        return $this->hasMany(GuestbookEntry::class);
    }
}
