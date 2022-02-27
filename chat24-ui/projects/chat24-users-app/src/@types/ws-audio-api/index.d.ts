/// <reference types="node" />
import { Socket } from 'ngx-socket-io';

declare const WSAudioAPI: WSAudioAPI.WSAudioAPI

declare namespace WSAudioAPI {
    interface Options {
        codec?: codec; 
        server?: server;
    }
    interface codec{
        sampleRate?: number;
        channels?: number;
        app?: number;
        frameDuration?: number;
        bufferSize?: number;

    }
    interface WSAudioAPI{
        Player:PlayerInstance;
        Streamer:StreamerInstance
    }
    interface server{
        host?:string;
        port?:number
    }
    interface Player {
        new (opts?: Options, socket?:Socket): PlayerInstance;
        (opts?: Options): PlayerInstance;
    }
    interface Streamer {
        new (opts?: Options): StreamerInstance;
        (opts?: Options): StreamerInstance;
    }
    interface PlayerInstance  {
        start(onError:Function): void;
        mute(): void;
        unMute(): void;
        onError(e:any): void;
        stop(): void;
    }
    interface StreamerInstance  {
        start(): void;
        getVolume(): void;
        setVolume(value:any): void;
        stop(): void;
    }
}

export = WSAudioAPI;